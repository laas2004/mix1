// import { NextRequest, NextResponse } from 'next/server';

// /**
//  * Ingest API - Proxies to Flask backend
//  * All file handling and pipeline execution happens in Flask
//  */
// export async function POST(req: NextRequest) {
//   try {
//     const formData = await req.formData();
    
//     // Forward to Flask backend
//     const response = await fetch('http://localhost:5000/api/admin/ingest', {
//       method: 'POST',
//       body: formData,
//     });
    
//     const result = await response.json();
    
//     return NextResponse.json(result, { status: response.status });
    
//   } catch (error) {
//     console.error('[INGEST] Proxy error:', error);
//     return NextResponse.json(
//       { success: false, error: error instanceof Error ? error.message : 'Ingest failed' },
//       { status: 500 }
//     );
//   }
// }


// import { NextResponse } from 'next/server';

// /**
//  * Ingest API - triggers ingestion pipeline
//  */
// export async function POST() {
//   try {

//     const response = await fetch('http://localhost:5000/api/admin/ingest', {
//       method: 'POST',
//     });

//     const result = await response.json();

//     return NextResponse.json(result, { status: response.status });

//   } catch (error) {
//     console.error('[INGEST] Proxy error:', error);

//     return NextResponse.json(
//       { success: false, error: 'Ingest failed' },
//       { status: 500 }
//     );
//   }
// }



// import { NextRequest, NextResponse } from 'next/server';

// export async function POST(req: NextRequest) {
//   try {
//     // Forward request as-is (no parsing)
//     const response = await fetch('http://localhost:5000/api/admin/ingest', {
//       method: 'POST',
//       headers: {
//         'Content-Type': req.headers.get('content-type') || '',
//       },
//       body: req.body,
//     });

//     const result = await response.json();

//     return NextResponse.json(result, { status: response.status });

//   } catch (error) {
//     console.error('[INGEST] Proxy error:', error);

//     return NextResponse.json(
//       { success: false, error: 'Backend ingestion service unavailable' },
//       { status: 500 }
//     );
//   }
// }



import { NextRequest, NextResponse } from 'next/server';

/**
 * Ingest API Proxy → Flask backend
 * Fully typed + no ESLint errors
 */

export async function POST(req: NextRequest) {
  try {
    const contentType = req.headers.get('content-type') ?? '';

    let body: BodyInit | undefined;

    // Handle multipart form data
    if (contentType.includes('multipart/form-data')) {
      const formData = await req.formData();

      const forwardedForm = new FormData();

      for (const [key, value] of formData.entries()) {
        if (value instanceof File || typeof value === 'string') {
          forwardedForm.append(key, value);
        }
      }

      body = forwardedForm;
    }

    /**
     * Cast to unknown first to allow duplex
     * (Node fetch supports it, TS types don't yet)
     */
    const fetchOptions = {
      method: 'POST',
      body,
      duplex: 'half',
    } as unknown as RequestInit;

    const response = await fetch(
      'http://localhost:5000/api/admin/ingest',
      fetchOptions
    );

    const result = await response.json();

    return NextResponse.json(result, { status: response.status });

  } catch (error) {
    console.error('[INGEST] Proxy error:', error);

    return NextResponse.json(
      {
        success: false,
        error:
          error instanceof Error ? error.message : 'Ingest failed',
      },
      { status: 500 }
    );
  }
}

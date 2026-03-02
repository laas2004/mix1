// import { NextRequest, NextResponse } from 'next/server';

// const FLASK_API_URL = process.env.FLASK_API_URL || 'http://localhost:5000';

// export async function POST(request: NextRequest) {
//   try {
//     const body = await request.json();
    
//     const response = await fetch(`${FLASK_API_URL}/api/query`, {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json',
//       },
//       body: JSON.stringify(body),
//     });

//     const data = await response.json();

//     if (!response.ok) {
//       return NextResponse.json(
//         { error: data.error || 'Query failed' },
//         { status: response.status }
//       );
//     }

//     return NextResponse.json(data);
//   } catch (error) {
//     console.error('API route error:', error);
//     return NextResponse.json(
//       { error: 'Failed to connect to backend service' },
//       { status: 500 }
//     );
//   }
// }


// import { NextRequest, NextResponse } from "next/server";

// export async function POST(req: NextRequest) {
//   const body = await req.json();

//   const res = await fetch("http://localhost:5000/query", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify(body),
//   });

//   const data = await res.json();

//   return NextResponse.json(data);
// }

// import { NextRequest, NextResponse } from "next/server";

// export async function POST(req: NextRequest) {
//   try {
//     const body = await req.json();

//     const res = await fetch("http://localhost:5000/query", {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify(body),
//     });

//     const data = await res.json();

//     // Ensure UI-compatible structure
//     return NextResponse.json({
//       result: {
//         synthesized_answer: data.answer || "",
//         answer_citations: data.citations || [],
//         retrieved_sections: data.sections || [],
//       },
//     });

//   } catch (error) {
//     console.error("Query route error:", error);

//     return NextResponse.json(
//       { error: "Failed to connect to backend" },
//       { status: 500 }
//     );
//   }
// }


import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();

    const res = await fetch("http://localhost:5000/query", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    const data = await res.json();

    return NextResponse.json({
      result: {
        synthesized_answer: data.answer || "",
        answer_citations: data.citations || [],
        retrieved_sections: data.sections || [],
      },
    });

  } catch (error) {
    console.error("Query route error:", error);

    return NextResponse.json(
      { error: "Backend connection failed" },
      { status: 500 }
    );
  }
}

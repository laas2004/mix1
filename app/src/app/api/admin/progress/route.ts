import { NextResponse } from "next/server"

export async function GET() {
  try {
    const response = await fetch("http://127.0.0.1:5000/api/pipeline/status")

    if (!response.ok) {
      throw new Error("Failed to fetch status")
    }

    const data = await response.json()

    return NextResponse.json(data)

  } catch (error) {
    console.error("[PROGRESS ERROR]", error)

    return NextResponse.json(
      { error: "Failed to fetch progress" },
      { status: 500 }
    )
  }
}
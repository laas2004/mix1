"use client"

import { useState } from "react"

export default function IngestionPage() {
  const [files, setFiles] = useState<FileList | null>(null)
  const [status, setStatus] = useState("")

  const handleUpload = async () => {
    if (!files) return

    const formData = new FormData()

    Array.from(files).forEach((file) => {
      formData.append("files", file)
    })

    setStatus("Uploading...")

    const res = await fetch("http://localhost:5000/api/admin/ingest", {
      method: "POST",
      body: formData,
    })

    const data = await res.json()

    if (data.success) {
      setStatus("✅ Ingestion completed")
    } else {
      setStatus("❌ Failed: " + data.error)
    }
  }

  return (
    <div className="flex flex-col items-center mt-20 gap-4">
      <h1 className="text-2xl font-bold">Admin Document Upload</h1>

      <input
        type="file"
        multiple
        accept=".pdf"
        onChange={(e) => setFiles(e.target.files)}
      />

      <button
        className="px-4 py-2 bg-green-600 text-white rounded"
        onClick={handleUpload}
      >
        Upload & Ingest
      </button>

      <p>{status}</p>
    </div>
  )
}

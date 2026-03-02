'use client';

import { useState } from 'react';

export default function SimpleIngestionPanel() {
  const [file, setFile] = useState<File | null>(null);
  const [logs, setLogs] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert('Select a PDF first');

    const formData = new FormData();
    formData.append('file', file);

    setLoading(true);

    try {
      const res = await fetch('/api/admin/upload', {
        method: 'POST',
        body: formData,
      });

      const data = await res.json();

      if (data.success) {
        setLogs((prev) => [...prev, `Uploaded: ${file.name}`]);
      } else {
        setLogs((prev) => [...prev, `Upload failed`]);
      }

    } catch {
      setLogs((prev) => [...prev, `Upload error`]);
    }

    setLoading(false);
  };

  const handleIngest = async () => {
    setLoading(true);

    try {
      const res = await fetch('/api/admin/ingest', {
        method: 'POST',
      });

      const data = await res.json();

      if (data.success) {
        setLogs((prev) => [...prev, 'Ingestion started']);
      } else {
        setLogs((prev) => [...prev, 'Ingestion failed']);
      }

    } catch {
      setLogs((prev) => [...prev, 'Ingestion error']);
    }

    setLoading(false);
  };

  return (
    <div className="bg-white rounded-xl border border-gray-200 p-6 space-y-6">

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Upload PDF
        </label>

        <input
          type="file"
          accept="application/pdf"
          onChange={(e) => setFile(e.target.files?.[0] || null)}
          className="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg p-2 bg-white"
        />
      </div>

      <div className="flex gap-4">
        <button
          onClick={handleUpload}
          disabled={loading}
          className="px-5 py-2 bg-orange-500 text-white rounded-lg hover:bg-orange-600"
        >
          Upload Document
        </button>

        <button
          onClick={handleIngest}
          disabled={loading}
          className="px-5 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-800"
        >
          Run Ingestion
        </button>
      </div>

      <div className="bg-gray-900 text-green-400 font-mono rounded-lg p-4 h-40 overflow-auto text-sm">
        {logs.length === 0 && <p className="text-gray-400">Pipeline logs…</p>}
        {logs.map((log, i) => (
          <p key={i}>{log}</p>
        ))}
      </div>

    </div>
  );
}

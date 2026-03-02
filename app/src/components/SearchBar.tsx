"use client";

import { useState } from "react";

export type SearchBarProps = {
  onSearch: (query: string) => Promise<void> | void;
  loading: boolean;
};

export default function SearchBar({ onSearch, loading }: SearchBarProps) {
  const [query, setQuery] = useState("");

  const handleSubmit = () => {
    if (!query.trim()) return;
    onSearch(query);
  };

  return (
    <div className="flex gap-2">
      <input
        className="flex-1 p-3 rounded text-black"
        placeholder="Ask a question..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && handleSubmit()}
      />

      <button
        onClick={handleSubmit}
        disabled={loading}
        className="bg-blue-600 px-4 rounded text-white"
      >
        {loading ? "Searching..." : "Search"}
      </button>
    </div>
  );
}

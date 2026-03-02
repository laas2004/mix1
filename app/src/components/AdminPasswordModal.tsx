// "use client";

// import { useState } from "react";

// type Props = {
//   onSuccess: () => void;
// };

// export default function AdminPasswordModal({ onSuccess }: Props) {
//   const [password, setPassword] = useState("");
//   const [error, setError] = useState("");

//   const ADMIN_PASSWORD = "admin123"; // change later

//   const handleSubmit = () => {
//     if (password === ADMIN_PASSWORD) {
//       onSuccess();
//     } else {
//       setError("Incorrect password");
//     }
//   };

//   return (
//     <div className="fixed inset-0 bg-black/60 flex items-center justify-center z-50">
//       <div className="bg-white text-black p-6 rounded-xl w-80 space-y-4">
//         <h2 className="text-lg font-semibold">Admin Authentication</h2>

//         <input
//           type="password"
//           placeholder="Enter password"
//           className="w-full border p-2 rounded"
//           value={password}
//           onChange={(e) => setPassword(e.target.value)}
//         />

//         {error && <p className="text-red-600 text-sm">{error}</p>}

//         <button
//           onClick={handleSubmit}
//           className="w-full bg-blue-600 text-white py-2 rounded"
//         >
//           Login
//         </button>
//       </div>
//     </div>
//   );
// }

"use client"

import { useState } from "react"

type Props = {
  onSuccess: () => void
  onClose: () => void
}

export default function AdminPasswordModal({ onSuccess, onClose }: Props) {
  const [password, setPassword] = useState("")
  const [error, setError] = useState("")

  const handleSubmit = () => {
    if (password === "admin123") {
      onSuccess()
    } else {
      setError("Incorrect password")
    }
  }

  return (
    <div className="fixed inset-0 bg-black/60 flex items-center justify-center z-50">

      <div className="bg-gray-900 p-6 rounded-xl w-96 border border-gray-700">

        <h2 className="text-lg font-semibold mb-4">Admin Login</h2>

        <input
          type="password"
          placeholder="Enter password"
          className="w-full p-2 rounded bg-gray-800 border border-gray-600 mb-3"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        {error && <p className="text-red-400 text-sm mb-2">{error}</p>}

        <div className="flex justify-end gap-2">

          <button
            onClick={onClose}
            className="px-4 py-2 bg-gray-700 rounded hover:bg-gray-600"
          >
            Cancel
          </button>

          <button
            onClick={handleSubmit}
            className="px-4 py-2 bg-blue-600 rounded hover:bg-blue-500"
          >
            Login
          </button>

        </div>

      </div>
    </div>
  )
}

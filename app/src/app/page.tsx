// 'use client';

// import { useRouter } from 'next/navigation';
// import { FaBalanceScale, FaUser, FaUserTie } from 'react-icons/fa';
// import { HiChevronRight } from 'react-icons/hi';

// export default function Home() {
//   const router = useRouter();

//   const handleProfileSelect = (profile: 'user' | 'admin') => {
//     router.push(`/${profile}`);
//   };

//   return (
//     <div className="min-h-screen bg-linear-to-br from-blue-900 via-blue-800 to-blue-900 flex items-center justify-center p-5">
//       <div className="max-w-4xl w-full">
//         {/* Header */}
//         <div className="text-center text-white mb-12">
//           <div className="flex items-center justify-center gap-3 mb-4">
//             <FaBalanceScale className="text-6xl" />
//             <h1 className="text-6xl font-bold drop-shadow-lg">
//               Pragya - Company Law
//             </h1>
//           </div>
//           <p className="text-2xl opacity-90 mb-2">CompanyGPT</p>
//           <p className="text-lg opacity-75">Select your profile to continue</p>
//         </div>

//         {/* Profile Selection */}
//         <div className="grid md:grid-cols-2 gap-8">
//           {/* User Profile */}
//           <button
//             onClick={() => handleProfileSelect('user')}
//             className="bg-white rounded-2xl p-10 shadow-2xl hover:shadow-3xl transform hover:-translate-y-2 transition-all duration-300 text-left group"
//           >
//             <div className="text-6xl mb-6 text-blue-800 group-hover:scale-110 transition-transform duration-300">
//               <FaUser />
//             </div>
//             <h2 className="text-3xl font-bold text-gray-900 mb-3">User</h2>
//             <p className="text-gray-600 text-lg leading-relaxed">
//               Search and explore the Companies Act 2013 with AI-powered insights and legal document retrieval.
//             </p>
//             <div className="mt-6 flex items-center text-blue-800 font-semibold">
//               <span>Continue as User</span>
//               <HiChevronRight className="w-5 h-5 ml-2 group-hover:translate-x-2 transition-transform" />
//             </div>
//           </button>

//           {/* Admin Profile */}
//           <button
//             onClick={() => handleProfileSelect('admin')}
//             className="bg-white rounded-2xl p-10 shadow-2xl hover:shadow-3xl transform hover:-translate-y-2 transition-all duration-300 text-left group"
//           >
//             <div className="text-6xl mb-6 text-blue-800 group-hover:scale-110 transition-transform duration-300">
//               <FaUserTie />
//             </div>
//             <h2 className="text-3xl font-bold text-gray-900 mb-3">Admin</h2>
//             <p className="text-gray-600 text-lg leading-relaxed">
//               Advanced features including system management, analytics, and administrative controls.
//             </p>
//             <div className="mt-6 flex items-center text-blue-800 font-semibold">
//               <span>Continue as Admin</span>
//               <HiChevronRight className="w-5 h-5 ml-2 group-hover:translate-x-2 transition-transform" />
//             </div>
//           </button>
//         </div>

//         {/* Footer Info */}
//         <div className="text-center text-white mt-12 opacity-75">
//           <p className="text-sm">
//             Powered by RAG Technology • AI-Enhanced Legal Research
//           </p>
//         </div>
//       </div>
//     </div>
//   );
// }


"use client"

import { useRouter } from "next/navigation"
import AdminPasswordModal from "../components/AdminPasswordModal"
import { useState } from "react"

export default function Home() {
  const router = useRouter()
  const [showAdminModal, setShowAdminModal] = useState(false)

  return (
    <main className="min-h-screen bg-gradient-to-br from-gray-900 to-gray-800 text-white flex flex-col items-center justify-center">

      <h1 className="text-4xl font-bold mb-12">Legal RAG Assistant</h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">

        {/* Employee */}
        <div
          onClick={() => router.push("/user")}
          className="cursor-pointer p-8 bg-gray-800 rounded-2xl border border-gray-700 hover:border-blue-500 transition"
        >
          <h2 className="text-xl font-semibold mb-2">Employee</h2>
          <p className="text-gray-400">Ask compliance questions</p>
        </div>

        {/* Junior HR */}
        <div
          onClick={() => router.push("/user")}
          className="cursor-pointer p-8 bg-gray-800 rounded-2xl border border-gray-700 hover:border-blue-500 transition"
        >
          <h2 className="text-xl font-semibold mb-2">Junior HR</h2>
          <p className="text-gray-400">Policy assistance</p>
        </div>

        {/* Admin */}
        <div
          onClick={() => setShowAdminModal(true)}
          className="cursor-pointer p-8 bg-gray-800 rounded-2xl border border-gray-700 hover:border-red-500 transition"
        >
          <h2 className="text-xl font-semibold mb-2">Admin</h2>
          <p className="text-gray-400">Upload & ingest documents</p>
        </div>

      </div>

      {showAdminModal && (
        <AdminPasswordModal
          onSuccess={() => router.push("/admin")}
          onClose={() => setShowAdminModal(false)}
        />
      )}

    </main>
  )
}

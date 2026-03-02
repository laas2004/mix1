// 'use client';

// import { Suspense } from 'react';
// import { useRouter, useSearchParams } from 'next/navigation';
// import AdminSidebar from '@/components/admin/AdminSidebar';
// import SimpleIngestionPanel from '@/components/admin/SimpleIngestionPanel';
// import PipelineStatus from '@/components/admin/PipelineStatus';
// import AuditTab from '@/components/admin/AuditTab';
// import NotificationsTab from '@/components/admin/NotificationsTab';
// import DashboardTab from '@/components/admin/DashboardTab';
// import AnalyticsTab from '@/components/admin/AnalyticsTab';
// import SystemHealthTab from '@/components/admin/SystemHealthTab';
// import ChatTab from '@/components/admin/ChatTab';
// import DocumentsTab from '@/components/admin/DocumentsTab';
// import SettingsTab from '@/components/admin/SettingsTab';

// function AdminPageContent() {
//   const router = useRouter();
//   const searchParams = useSearchParams();
//   const activeTab = searchParams.get('tab') || 'dashboard';


//   // Update URL when tab changes
//   const handleTabChange = (tab: string) => {
//     router.push(`/admin?tab=${tab}`, { scroll: false });
//   };

//   const renderContent = () => {
//     switch (activeTab) {
//       case 'dashboard':
//         return <DashboardTab />;
      
//       case 'ingestion':
//         return (
//     <div className="space-y-6">
//       <div>
//         <h2 className="text-2xl font-bold text-gray-900">
//           Document Ingestion
//         </h2>
//         <p className="text-gray-600 mt-1">
//           Upload and process documents into the knowledge base
//         </p>
//       </div>

//       <PipelineStatus />

//       <SimpleIngestionPanel />
//     </div>
//   );
      
//       case 'audit':
//         return <AuditTab />;
      
//       case 'notifications':
//         return <NotificationsTab />;
      
//       case 'analytics':
//         return <AnalyticsTab />;
      
//       case 'health':
//         return <SystemHealthTab />;
      
//       case 'chat':
//         return <ChatTab />;
      
//       case 'documents':
//         return <DocumentsTab />;
      
//       case 'settings':
//         return <SettingsTab />;
      
//       default:
//         return <DashboardTab />;
//     }
//   };

//   return (
//     <div className="min-h-screen bg-gray-50 flex">
//       {/* Sidebar - Fixed position */}
//       <div className="w-64 shrink-0">
//         <div className="fixed top-0 left-0 h-screen w-64 z-20">
//           <AdminSidebar activeTab={activeTab} onTabChange={handleTabChange} />
//         </div>
//       </div>

//       {/* Main Content */}
//       <div className="flex-1 overflow-auto">
//         {/* Top Header */}
//         <header className="bg-white border-b border-gray-200 px-8 py-4 flex items-center justify-between sticky top-0 z-10">
//           <div>
//             <h1 className="text-xl font-semibold text-gray-900 capitalize">
//               {activeTab === 'health' ? 'System Health' : activeTab}
//             </h1>
//             <p className="text-sm text-gray-500">
//               {new Date().toLocaleDateString('en-IN', { 
//                 weekday: 'long', 
//                 year: 'numeric', 
//                 month: 'long', 
//                 day: 'numeric' 
//               })}
//             </p>
//           </div>
//           <div className="flex items-center gap-4">
//             <div className="text-right">
//               <p className="text-sm font-medium text-gray-900">Welcome back</p>
//               <p className="text-xs text-gray-500">Administrator</p>
//             </div>
//             <div className="w-10 h-10 bg-linear-to-br from-orange-400 to-orange-600 rounded-full flex items-center justify-center text-white font-semibold">
//               A
//             </div>
//           </div>
//         </header>

//         {/* Page Content */}
//         <main className="p-8">
//           {renderContent()}
//         </main>
//       </div>
//     </div>
//   );
// }

// // Wrap with Suspense for useSearchParams
// export default function AdminPage() {
//   return (
//     <Suspense fallback={
//       <div className="min-h-screen bg-gray-50 flex items-center justify-center">
//         <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-orange-500"></div>
//       </div>
//     }>
//       <AdminPageContent />
//     </Suspense>
//   );
// }



//abv original
'use client';

import { Suspense, useState, useEffect } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';
import AdminSidebar from '@/components/admin/AdminSidebar';
import SimpleIngestionPanel from '@/components/admin/SimpleIngestionPanel';
import PipelineStatus from '@/components/admin/PipelineStatus';
import AuditTab from '@/components/admin/AuditTab';
import NotificationsTab from '@/components/admin/NotificationsTab';
import DashboardTab from '@/components/admin/DashboardTab';
import AnalyticsTab from '@/components/admin/AnalyticsTab';
import SystemHealthTab from '@/components/admin/SystemHealthTab';
import ChatTab from '@/components/admin/ChatTab';
import DocumentsTab from '@/components/admin/DocumentsTab';
import SettingsTab from '@/components/admin/SettingsTab';

function AdminPageContent() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const activeTab = searchParams.get('tab') || 'dashboard';

  // State variables for progress tracking
  const [progressStatus, setProgressStatus] = useState<string>('');
  const [isCheckingProgress, setIsCheckingProgress] = useState(false);

  // Update URL when tab changes
  const handleTabChange = (tab: string) => {
    router.push(`/admin?tab=${tab}`, { scroll: false });
  };

  // Progress handler function
  const handleCheckProgress = async () => {
    setIsCheckingProgress(true);
    setProgressStatus('Checking pipeline status...');

    try {
      const res = await fetch('/api/admin/progress');       //http://127.0.0.1:5000/api/pipeline/status

      if (!res.ok) {
        throw new Error('Failed to fetch status');
      }

      const data = await res.json();

      const statusText = `
Status: ${data.running ? 'Running' : 'Idle'}
Message: ${data.message}
Last Run: ${data.last_run ?? 'N/A'}
      `;

      setProgressStatus(statusText);
    } catch (err) {
      console.error(err);
      setProgressStatus('Failed to fetch progress');
    } finally {
      setIsCheckingProgress(false);
    }
  };

  // Auto-refresh progress every 5 seconds (optional)
  useEffect(() => {
    const interval = setInterval(() => {
      handleCheckProgress();
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  const renderContent = () => {
    switch (activeTab) {
      case 'dashboard':
        return <DashboardTab />;
      case 'ingestion':
        return (
          <div className="space-y-6">
            <div>
              <h2 className="text-2xl font-bold text-gray-900">Document Ingestion</h2>
              <p className="text-gray-600 mt-1">Upload and process documents into the knowledge base</p>
            </div>
            <PipelineStatus />
            <SimpleIngestionPanel />
            {/* Add Progress Check Button */}
            <button
              onClick={handleCheckProgress}
              disabled={isCheckingProgress}
              className="px-4 py-2 bg-blue-600 hover:bg-blue-700 rounded-md text-white"
            >
              {isCheckingProgress ? 'Checking...' : 'Check Progress'}
            </button>

            {/* Display Progress Status */}
            {progressStatus && (
              <div className="mt-4 p-3 bg-gray-800 rounded-md text-gray-200 whitespace-pre-line">
                {progressStatus}
              </div>
            )}
          </div>
        );
      case 'audit':
        return <AuditTab />;
      case 'notifications':
        return <NotificationsTab />;
      case 'analytics':
        return <AnalyticsTab />;
      case 'health':
        return <SystemHealthTab />;
      case 'chat':
        return <ChatTab />;
      case 'documents':
        return <DocumentsTab />;
      case 'settings':
        return <SettingsTab />;
      default:
        return <DashboardTab />;
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 flex">
      {/* Sidebar - Fixed position */}
      <div className="w-64 shrink-0">
        <div className="fixed top-0 left-0 h-screen w-64 z-20">
          <AdminSidebar activeTab={activeTab} onTabChange={handleTabChange} />
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 overflow-auto">
        {/* Top Header */}
        <header className="bg-white border-b border-gray-200 px-8 py-4 flex items-center justify-between sticky top-0 z-10">
          <div>
            <h1 className="text-xl font-semibold text-gray-900 capitalize">
              {activeTab === 'health' ? 'System Health' : activeTab}
            </h1>
            <p className="text-sm text-gray-500">
              {new Date().toLocaleDateString('en-IN', {
                weekday: 'long',
                year: 'numeric',
                month: 'long',
                day: 'numeric',
              })}
            </p>
          </div>
          <div className="flex items-center gap-4">
            <div className="text-right">
              <p className="text-sm font-medium text-gray-900">Welcome back</p>
              <p className="text-xs text-gray-500">Administrator</p>
            </div>
            <div className="w-10 h-10 bg-linear-to-br from-orange-400 to-orange-600 rounded-full flex items-center justify-center text-white font-semibold">
              A
            </div>
          </div>
        </header>

        {/* Page Content */}
        <main className="p-8">{renderContent()}</main>
      </div>
    </div>
  );
}

// Wrap with Suspense for useSearchParams
export default function AdminPage() {
  return (
    <Suspense
      fallback={
        <div className="min-h-screen bg-gray-50 flex items-center justify-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-orange-500"></div>
        </div>
      }
    >
      <AdminPageContent />
    </Suspense>
  );
}
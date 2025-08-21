import React from 'react';
import MessageList from './components/MessageList';
import useApi from './hooks/useApi';
import MetricsDashboard from './components/MetricsDashboard';

const App: React.FC = () => {
  const { messages, metrics, loading, error } = useApi();

  if (loading) return <div className="p-4 text-center">Loading...</div>;
  if (error) return <div className="p-4 text-red-500 text-center">{error}</div>;

  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-blue-600 text-white p-4 text-center">
        <h1 className="text-2xl font-bold">SamrakshIQ Message Review</h1>
      </header>
      <main>
        <MessageList messages={messages} />
        <MetricsDashboard metrics={metrics} />
      </main>
    </div>
  );
};

export default App;
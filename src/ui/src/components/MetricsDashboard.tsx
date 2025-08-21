import React from 'react';

interface Metrics {
  redactTime: number;
  hashTime: number;
  pseudoTime: number;
  fpeTime: number;
  aesTime: number;
}

const MetricsDashboard: React.FC<{ metrics: Metrics }> = ({ metrics }) => {
  return (
    <div className="p-4 max-w-2xl mx-auto mt-4 bg-white rounded-lg shadow">
      <h2 className="text-lg font-semibold mb-2">Performance Metrics (ms)</h2>
      <ul className="space-y-2">
        <li>Redaction: {metrics.redactTime.toFixed(10)}</li>
        <li>Hashing: {metrics.hashTime.toFixed(10)}</li>
        <li>Pseudonymization: {metrics.pseudoTime.toFixed(10)}</li>
        <li>FPE: {metrics.fpeTime.toFixed(10)}</li>
        <li>AES: {metrics.aesTime.toFixed(10)}</li>
      </ul>
    </div>
  );
};

export default MetricsDashboard;
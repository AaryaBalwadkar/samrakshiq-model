import { useState, useEffect } from 'react';

interface Message {
  id: number;
  text: string;
}

interface Metrics {
  redactTime: number;
  hashTime: number;
  pseudoTime: number;
  fpeTime: number;
  aesTime: number;
}

interface ApiResponse {
  messages: Message[];
  metrics: Metrics;
}

const useApi = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [metrics, setMetrics] = useState<Metrics>({
    redactTime: 0,
    hashTime: 0,
    pseudoTime: 0,
    fpeTime: 0,
    aesTime: 0,
  });
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/messages');
        if (!response.ok) throw new Error('Failed to fetch');
        const data: ApiResponse = await response.json();
        setMessages(data.messages);
        setMetrics(data.metrics);
      } catch (err) {
        setError((err as Error).message);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  return { messages, metrics, loading, error };
};

export default useApi;
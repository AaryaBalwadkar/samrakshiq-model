import { useState } from 'react';
import axios from 'axios';

interface ApiResponse {
  data: any;
  fetch: (url: string) => Promise<void>;
}

export function useApi(): ApiResponse {
  const [data, setData] = useState<any>(null);
  const fetch = async (url: string) => {
    const res = await axios.get(url);
    setData(res.data);
  };
  return { data, fetch };
}
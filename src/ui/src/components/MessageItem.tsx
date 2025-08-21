import React from 'react';

interface MessageItemProps {
  message: string;
}

const MessageItem: React.FC<MessageItemProps> = ({ message }) => {
  return (
    <div className="mb-4 p-3 border border-gray-300 rounded-lg shadow-sm hover:bg-gray-50 transition">
      <p className="text-sm text-gray-700">{message}</p>
    </div>
  );
};

export default MessageItem;
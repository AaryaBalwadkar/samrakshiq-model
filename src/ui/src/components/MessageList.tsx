import React from 'react';
import MessageItem from './MessageItem';

interface Message {
  id: number;
  text: string;
}

interface MessageListProps {
  messages: Message[];
}

const MessageList: React.FC<MessageListProps> = ({ messages }) => {
  return (
    <div className="p-4 max-w-2xl mx-auto">
      {messages.length > 0 ? (
        messages.map((msg) => (
          <MessageItem key={msg.id} message={msg.text} />
        ))
      ) : (
        <p className="text-gray-500">No messages to display.</p>
      )}
    </div>
  );
};

export default MessageList;
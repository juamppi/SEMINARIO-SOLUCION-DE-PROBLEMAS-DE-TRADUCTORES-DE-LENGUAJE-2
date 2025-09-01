// components/restaurant/login-form.tsx
import React, { useState } from 'react';
import { Button } from '../ui/button';

interface LoginFormProps {
  onLogin: (workerId: string) => void;
}

export const LoginForm: React.FC<LoginFormProps> = ({ onLogin }) => {
  const [workerId, setWorkerId] = useState('');
  
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (workerId.trim()) {
      onLogin(workerId.trim());
    }
  };
  
  return (
    <div className="max-w-md mx-auto bg-white rounded-lg shadow-lg p-6">
      <h2 className="text-2xl font-bold text-center mb-6 text-gray-800">
        Iniciar Sesión - Restaurante
      </h2>
      
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            ID del Trabajador
          </label>
          <input
            type="text"
            value={workerId}
            onChange={(e) => setWorkerId(e.target.value)}
            placeholder="Ej: 1111"
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-orange-500"
            required
          />
        </div>
        
        <Button type="submit" className="w-full">
          Ingresar
        </Button>
      </form>
    </div>
  );
};
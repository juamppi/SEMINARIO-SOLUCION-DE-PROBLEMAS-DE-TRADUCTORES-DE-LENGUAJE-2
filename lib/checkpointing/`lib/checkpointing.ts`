// lib/checkpointing.ts
export interface OrderItem {
  id: string;
  name: string;
  quantity: number;
  price: number;
  notes?: string;
}

export interface CheckpointData {
  workerId: string;
  tableId: string;
  items: OrderItem[];
  timestamp: number;
  status: 'in-progress' | 'completed' | 'abandoned';
}

export class CheckpointManager {
  private static STORAGE_KEY = 'restaurant_checkpoints';
  
  // Guardar checkpoint
  static saveCheckpoint(data: CheckpointData): void {
    const checkpoints = this.getAllCheckpoints();
    const key = `${data.workerId}_${data.tableId}`;
    checkpoints[key] = data;
    localStorage.setItem(this.STORAGE_KEY, JSON.stringify(checkpoints));
  }
  
  // Recuperar checkpoint específico
  static getCheckpoint(workerId: string, tableId: string): CheckpointData | null {
    const checkpoints = this.getAllCheckpoints();
    const key = `${workerId}_${tableId}`;
    return checkpoints[key] || null;
  }
  
  // Obtener todos los checkpoints
  static getAllCheckpoints(): Record<string, CheckpointData> {
    const stored = localStorage.getItem(this.STORAGE_KEY);
    return stored ? JSON.parse(stored) : {};
  }
  
  // Obtener órdenes pendientes de otros usuarios
  static getPendingOrders(currentWorkerId: string): CheckpointData[] {
    const checkpoints = this.getAllCheckpoints();
    return Object.values(checkpoints).filter(
      checkpoint => 
        checkpoint.workerId !== currentWorkerId && 
        checkpoint.status === 'in-progress' &&
        checkpoint.items.length > 0
    );
  }
  
  // Tomar orden de otro usuario
  static takeOverOrder(originalWorkerId: string, tableId: string, newWorkerId: string): void {
    const checkpoint = this.getCheckpoint(originalWorkerId, tableId);
    if (checkpoint) {
      // Eliminar checkpoint original
      this.deleteCheckpoint(originalWorkerId, tableId);
      // Crear nuevo checkpoint con el nuevo trabajador
      checkpoint.workerId = newWorkerId;
      this.saveCheckpoint(checkpoint);
    }
  }
  
  // Eliminar checkpoint
  static deleteCheckpoint(workerId: string, tableId: string): void {
    const checkpoints = this.getAllCheckpoints();
    const key = `${workerId}_${tableId}`;
    delete checkpoints[key];
    localStorage.setItem(this.STORAGE_KEY, JSON.stringify(checkpoints));
  }
}
package fr.augusti.app.models;

public class Queue {
    private LinkedList data;

    public boolean isEmpty() {
        return this.data == null;
    }

    public Object peek() {
        if (!this.isEmpty()) {
            return this.data.data;
        }
        return null;
    }

    public Object dequeue() {
        if (!this.isEmpty()) {
            Object item = this.peek();
            this.data = this.data.next;
            return item;
        }
        return null;
    }

    public void enqueue(Object item) {
        if (this.isEmpty()) {
            this.data = new LinkedList(item);
        } else {
            this.data.appendToTail(item);
        }
    }
}

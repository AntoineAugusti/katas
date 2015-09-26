package fr.augusti.app.models;

public class Stack {
    private LinkedList top;

    public boolean isEmpty() {
        return this.top == null;
    }

    public Object pop() {
        if (!this.isEmpty()) {
            Object item = this.peek();
            top = top.next;
            return item;
        }
        return null;
    }

    public void push(Object item) {
        LinkedList t = new LinkedList(item);
        t.next = top;
        this.top = t;
    }

    public Object peek() {
        if (!this.isEmpty()) {
            return this.top.data;
        }
        return null;
    }
}

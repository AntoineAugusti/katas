package fr.augusti.app.models;

import java.lang.IllegalArgumentException;

public class LinkedList {
    protected Object data;
    protected LinkedList next;

    public LinkedList() {
        this.data = null;
        this.next = null;
    }

    public LinkedList(Object item) {
        this.data = item;
        this.next = null;
    }

    public boolean isEmpty() {
        return this.data == null;
    }

    public boolean hasNext() {
        return this.next != null;
    }

    public void append(Object item) {
        if (this.isEmpty()) {
            this.data = item;
        } else if (this.hasNext())  {
            throw new IllegalArgumentException("Has already next");
        } else {
            this.next = new LinkedList(item);
        }
    }

    public void appendToTail(Object item) {
        LinkedList end = new LinkedList(item);
        LinkedList current = this;
        while (current.hasNext()) {
            current = current.next;
        }
        current.next = end;
    }
}

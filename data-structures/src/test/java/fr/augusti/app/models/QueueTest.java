package fr.augusti.app.models;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import org.junit.Test;

public class QueueTest {
    @Test
    public void canCheckIfQueueIsEmptyOrNot() {
        Queue queue = new Queue();
        assertTrue(queue.isEmpty());

        queue.enqueue(42);

        assertFalse(queue.isEmpty());
    }

    @Test
    public void canPeekObject() {
        Queue queue = new Queue();
        queue.enqueue(42);
        assertEquals(42, queue.peek());
    }

    @Test
    public void orderIsCorrect() {
        Queue queue = new Queue();
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);

        assertEquals(1, queue.dequeue());
        assertEquals(2, queue.dequeue());
        assertEquals(3, queue.dequeue());
        assertNull(queue.dequeue());
        assertNull(queue.peek());
    }
}

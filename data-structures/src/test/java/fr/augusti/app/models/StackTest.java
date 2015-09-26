package fr.augusti.app.models;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;

public class StackTest {
    @Test
    public void canCheckIfStackIsEmptyOrNot() {
        Stack stack = new Stack();
        assertTrue(stack.isEmpty());

        stack.push(42);

        assertFalse(stack.isEmpty());
    }

    @Test
    public void canPeekObject() {
        Stack stack = new Stack();
        stack.push(42);
        assertEquals(42, stack.peek());
    }

    @Test
    public void orderIsCorrect() {
        Stack stack = new Stack();
        stack.push(1);
        stack.push(2);
        stack.push(3);

        assertEquals(3, stack.pop());
        assertEquals(2, stack.pop());
        assertEquals(1, stack.pop());
        assertNull(stack.pop());
        assertNull(stack.peek());
    }
}

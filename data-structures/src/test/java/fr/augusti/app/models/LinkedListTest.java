package fr.augusti.app.models;

import java.lang.IllegalArgumentException;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;

public class LinkedListTest {
    @Test
    public void canCheckIfLinkedListIsEmptyOrNot() {
        LinkedList list = new LinkedList();
        assertTrue(list.isEmpty());

        list.append(42);

        assertFalse(list.isEmpty());
    }

    @Test
    public void canCheckIfLinkedListHasNextOrNot() {
        LinkedList list = new LinkedList(13);
        assertFalse(list.hasNext());

        list.append(42);

        assertTrue(list.hasNext());
    }

    @Test
    public void canPeekObject() {
        LinkedList list = new LinkedList();
        list.append(42);

        assertEquals(42, list.data);
    }

    @Test
    public void canAppendToTail() {
        LinkedList list = new LinkedList(1);
        LinkedList head = list;
        list.append(2);
        list.next.append(3);
        head.appendToTail(4);

        assertEquals(1, head.data);
        assertEquals(2, head.next.data);
        assertEquals(3, head.next.next.data);
        assertEquals(4, head.next.next.next.data);
    }

    @Test(expected=IllegalArgumentException.class)
    public void cannotAppendMultipleTimes() {
        LinkedList list = new LinkedList(1);

        list.append(2);
        list.append(3);
    }
}

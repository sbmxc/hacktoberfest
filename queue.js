class Queue{
    constructor(){
        this.items = {};
        this.rear = 0;
        this.front = 0;
    }

    enqueue(element) {
        this.items[this.rear] = element;
        this.rear++;
    }
    
    dequeue() {
        const item = this.items[this.front];
        delete this.items[this.front];
        this.front++;
        return item
    }

    isEmpty() {
        return this.rear - this.front === 0;
    }
    
    peek() {
        return this.items[this.front];
    }

    size() {
        return this.rear - this.front;
    }

    print() {
        console.log(this.items);
    }
}

const queue = new Queue();

queue.enqueue(10);
queue.enqueue(20);
queue.enqueue(30);
queue.enqueue(40);
queue.enqueue(50);
console.log(queue.size());
queue.print();

console.log(queue.dequeue());
console.log(queue.peek());

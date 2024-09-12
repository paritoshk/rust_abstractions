package main

import (
	"fmt"
	"time"
)

func timedTask(task func(), name string, start time.Time) {
	taskStart := time.Now()
	fmt.Printf("%s started work: at %.1f seconds\n", name, taskStart.Sub(start).Seconds())
	task()
	taskEnd := time.Now()
	fmt.Printf("%s ended work: at %.1f seconds\n", name, taskEnd.Sub(start).Seconds())
}

func task1() {
	time.Sleep(2 * time.Second)
}

func task2() {
	time.Sleep(2 * time.Second)
}

func task3(start time.Time) {
	fmt.Printf("Task 3 kicks off when task1, task2 goroutines are blocked, at %.1f seconds\n", time.Since(start).Seconds())
	time.Sleep(1 * time.Second)
	fmt.Println("Task 3 is Done!")
}

func main() {
	start := time.Now()

	done := make(chan bool)

	go func() {
		timedTask(task1, "Task 1", start)
		done <- true
	}()

	go func() {
		timedTask(task2, "Task 2", start)
		done <- true
	}()

	go func() {
		timedTask(func() { task3(start) }, "Task 3", start)
		done <- true
	}()

	for i := 0; i < 3; i++ {
		<-done
	}

	fmt.Printf("Total execution time: %.1f seconds\n", time.Since(start).Seconds())
}
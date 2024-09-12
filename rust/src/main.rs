use std::time::{Duration, Instant};
use tokio::time::sleep;

async fn timed_task<F, Fut>(task: F, name: &str, start: Instant)
where
    F: FnOnce() -> Fut,
    Fut: std::future::Future<Output = ()>,
{
    let task_start = Instant::now();
    println!("{} started work: at {:.1} seconds", name, task_start.duration_since(start).as_secs_f32());
    task().await;
    let task_end = Instant::now();
    println!("{} ended work: at {:.1} seconds", name, task_end.duration_since(start).as_secs_f32());
}

async fn task1() {
    sleep(Duration::from_secs(2)).await;
}

async fn task2() {
    sleep(Duration::from_secs(2)).await;
}

async fn task3(start: Instant) {
    println!("Task 3 kicks off when task1, task2 futures are blocked, at {:.1} seconds", start.elapsed().as_secs_f32());
    sleep(Duration::from_secs(1)).await;
    println!("Task 3 is Done!");
}

#[tokio::main]
async fn main() {
    let start = Instant::now();

    let task1 = tokio::spawn(timed_task(task1, "Task 1", start));
    let task2 = tokio::spawn(timed_task(task2, "Task 2", start));
    let task3 = tokio::spawn(timed_task(move || task3(start), "Task 3", start));

    let _ = tokio::join!(task1, task2, task3);

    let end = Instant::now();
    println!("Total execution time: {:.3} seconds", end.duration_since(start).as_secs_f32());
}
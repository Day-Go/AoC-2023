use std::fs;

fn main() {
    let contexts = fs::read_to_string("input.txt")
        .expect("Error reading input.txt");

    let mut total = 0;
    for line in contexts.lines() {
        let mut num_str = String::from("");

        println!("{}\n", line);

        for c in line.chars() {
            if c.is_numeric() {
                num_str.push(c);
                break
            }
        }

        for c in line.chars().rev() {
            if c.is_numeric()  {
                num_str.push(c);
                break
            }
        }

        match num_str.parse::<i32>() {
            Ok(num) => total += num,
            Err(e) => println!("Failed to parse: {}", e),
        }
    }

    println!("{}", total)
}
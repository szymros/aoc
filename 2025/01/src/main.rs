fn part1(input: &str) -> i32 {
    let mut position: i32 = 50;
    let mut password = 0;
    input.lines().for_each(|line| {
        let (dir, digit) = line.split_at(1);
        let distance = digit.parse::<i32>().unwrap();
        if dir == "L" {
            position = (100 + position - distance) % 100;
        } else {
            position = (position + distance) % 100;
        }
        if position == 0 {
            password += 1;
        }
    });
    return password;
}

pub fn part2(input: &str) -> i32 {
    let mut position: i32 = 50;
    let mut password = 0;
    input.lines().for_each(|line| {
        let (dir, digits) = line.split_at(1);
        let distance = digits.parse::<i32>().unwrap();
        if dir == "L" {
            let pos = if position == 0 { 100 } else { position };
            let traveled = pos - distance;
            if traveled <= 0 {
                password += 1 + (traveled.abs() / 100);
            }
            position = (100 + traveled % 100) % 100;
        } else {
            let traveled = position + distance;
            if traveled >= 100 {
                password += traveled / 100;
            }
            position = traveled % 100;
        }
    });
    return password;
}

fn main() {
    let input = std::fs::read_to_string("input.txt").unwrap();
    println!("part 1 result {}", part1(&input));
    println!("part 2 result {}", part2(&input));
}

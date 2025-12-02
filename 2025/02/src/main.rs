fn part1(input: &str) -> i64 {
    let ranges: Vec<&str> = input.trim().split(",").collect();
    let mut output = 0;
    ranges.iter().for_each(|range| {
        let bounds: Vec<&str> = range.split("-").collect();
        let start = bounds[0].parse::<i64>().unwrap();
        let end = bounds[1].parse::<i64>().unwrap();
        for i in start..=end {
            let str_i = i.to_string();
            if str_i.len() % 2 != 0 {
                continue;
            }
            let mid = str_i.len() / 2;
            if str_i[..mid] == str_i[mid..] {
                output += i;
            }
        }
    });
    return output;
}

fn check_if_silly(num: &str) -> bool {
    for pattern_len in 1..=num.len() / 2 {
        if num.len() % pattern_len == 0 {
            let pattern = &num[..pattern_len];
            let mut silly = true;
            for i in (0..num.len()).step_by(pattern_len) {
                if *pattern != num[i..i + pattern_len] {
                    silly = false;
                    break;
                }
            }
            if silly {
                return true;
            }
        }
    }
    return false;
}

fn part2(input: &str) -> i64 {
    let ranges: Vec<&str> = input.trim().split(",").collect();
    let mut output = 0;
    ranges.iter().for_each(|range| {
        let bounds: Vec<&str> = range.split("-").collect();
        let start = bounds[0].parse::<i64>().unwrap();
        let end = bounds[1].parse::<i64>().unwrap();
        for i in start..=end {
            if check_if_silly(&i.to_string()) {
                output += i;
            }
        }
    });
    return output;
}

fn main() {
    let input = std::fs::read_to_string("input.txt").unwrap();
    println!("part 1 {}", part1(&input));
    println!("part 2 {}", part2(&input));
}

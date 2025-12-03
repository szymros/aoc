fn solve(input: &str, num_len: usize) -> i64 {
    let mut output = 0;
    input.lines().for_each(|line| {
        let mut nums: Vec<char> = Vec::new();
        let mut start_idx = 0;
        for i in (0..num_len).rev() {
            let mut largest_idx = 0;
            let mut largest_value: char = '0';
            for (idx, char) in line[start_idx..line.len() - i].char_indices() {
                if char > largest_value {
                    largest_value = char;
                    largest_idx = idx;
                }
            }
            start_idx += largest_idx + 1;
            nums.push(largest_value);
        }
        output += nums.iter().collect::<String>().parse::<i64>().unwrap();
    });
    return output;
}

fn main() {
    let input = std::fs::read_to_string("input.txt").unwrap();
    println!("part 1 {}", solve(&input, 2));
    println!("part 2 {}", solve(&input, 12));
}

fn part1(input: &str) -> i64 {
    let start = input.find("S").unwrap();
    let mut grid = input
        .lines()
        .map(|line| line.chars().collect::<Vec<char>>())
        .collect::<Vec<Vec<char>>>();

    let mut heads: Vec<(usize, usize)> = vec![(start, 0)];
    let mut num_splits = 0;

    while !heads.is_empty() {
        let (x, y) = heads[0];
        if grid[y][x] == '|' || y + 1 == grid.len() {
            heads = heads[1..].to_vec();
            continue;
        }
        grid[y][x] = '|';
        let next = grid[y + 1][x];
        if next == '^' {
            num_splits += 1;
            if x + 1 < grid[0].len() {
                heads.push((x + 1, y + 1));
            }
            if x > 0 {
                heads.push((x - 1, y + 1));
            }
        } else {
            heads.push((x, y + 1));
        }
        heads = heads[1..].to_vec();
    }

    return num_splits;
}

fn part2(input: &str) -> i64 {
    let start = input.find("S").unwrap();
    let mut grid = input
        .lines()
        .map(|line| line.chars().collect::<Vec<char>>())
        .collect::<Vec<Vec<char>>>();

    let len_line = grid[0].len();
    let mut heads: Vec<i64> = vec![0; len_line];
    heads[start] = 1;

    for line in grid[1..].iter() {
        let mut new_heads = vec![0; len_line];
        for (idx, v) in heads.iter().enumerate() {
            if line[idx] == '^' {
                if idx > 0 {
                    new_heads[idx - 1] += v;
                }
                if idx + 1 < len_line {
                    new_heads[idx + 1] += v;
                }
            } else {
                new_heads[idx] += v;
            }
        }
        heads = new_heads;
    }

    return heads.iter().sum();
}
fn main() {
    let input = std::fs::read_to_string("input.txt").unwrap();
    println!("part 1 {}", part1(&input));
    println!("part 2 {}", part2(&input));
}

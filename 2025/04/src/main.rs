#[rustfmt::skip]
const DIRECTIONS: [(i32, i32); 8] = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0),           (1, 0),
        (-1, 1),  (0, 1),  (1, 1)
];

fn num_neighbours(lines: &[String], current_line: &str, x: i32, y: i32) -> i32 {
    let mut neighbour_count = 0;
    for (dir_x, dir_y) in DIRECTIONS.iter() {
        let x_to_check = dir_x + x;
        let y_to_check = dir_y + y;
        if x_to_check < current_line.len() as i32
            && x_to_check >= 0
            && y_to_check < lines.len() as i32
            && y_to_check >= 0
            && lines[y_to_check as usize]
                .chars()
                .nth(x_to_check as usize)
                .unwrap()
                == '@'
        {
            neighbour_count += 1;
        }
    }
    return neighbour_count;
}

fn part1(lines: &[String]) -> i32 {
    let mut output = 0;
    lines.iter().enumerate().for_each(|(y, slice)| {
        let mut slice_x = 0;
        while let Some(x) = (slice[slice_x..]).find('@') {
            let current_x = x + slice_x;
            slice_x = current_x + 1;
            let neighbouts_count = num_neighbours(lines, slice, current_x as i32, y as i32);
            if neighbouts_count < 4 {
                output += 1;
            }
        }
    });
    return output;
}

fn part2(lines: Vec<String>) -> i32 {
    let mut output = 0;
    let mut lines = lines;
    let mut accessible: Vec<(usize, usize)> = Vec::new();
    loop {
        lines.iter().enumerate().for_each(|(y, slice)| {
            let mut slice_x = 0;
            while let Some(x) = (slice[slice_x..]).find('@') {
                let current_x = x + slice_x;
                slice_x = current_x + 1;
                let neighbouts_count = num_neighbours(&lines, slice, current_x as i32, y as i32);
                if neighbouts_count < 4 {
                    output += 1;
                    accessible.push((current_x, y));
                }
            }
        });
        if accessible.is_empty() {
            break;
        }
        for (x, y) in accessible.iter() {
            let mut chars = lines[*y].chars().collect::<Vec<char>>();
            chars[*x] = '.';
            let s = chars.iter().collect::<String>();
            lines[*y] = s;
        }
        accessible = vec![];
    }
    return output;
}

fn main() {
    let f = std::fs::read_to_string("input.txt").unwrap();
    let lines = f.lines().map(|s| s.to_string()).collect::<Vec<String>>();
    println!("part 1 {}", part1(&lines));
    println!("part 2 {}", part2(lines));
}

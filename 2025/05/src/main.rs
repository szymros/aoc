use std::ops::RangeInclusive;

pub fn part1(input: &str) -> i64 {
    let mut ranges: Vec<RangeInclusive<i64>> = Vec::new();
    let mut fresh_ids: Vec<i64> = Vec::new();
    input.lines().for_each(|line| {
        if line.contains('-') {
            let s = line.split('-').collect::<Vec<&str>>();
            let start = s[0].parse::<i64>().unwrap();
            let end = s[1].parse::<i64>().unwrap();
            ranges.push(start..=end);
        } else if !line.is_empty() {
            fresh_ids.push(line.parse::<i64>().unwrap());
        }
    });
    let mut output = 0;
    for id in fresh_ids.iter() {
        for range in ranges.iter() {
            if range.contains(id) {
                output += 1;
                break;
            }
        }
    }
    return output;
}

fn part2(input: &str) -> i64 {
    let mut ranges: Vec<RangeInclusive<i64>> = Vec::new();
    input.lines().for_each(|line| {
        if line.contains('-') {
            let splits = line.split('-').collect::<Vec<&str>>();
            let start = splits[0].parse::<i64>().unwrap();
            let end = splits[1].parse::<i64>().unwrap();
            ranges.push(start..=end);
        }
    });

    let mut merged: Vec<RangeInclusive<i64>> = Vec::new();
    ranges.sort_by(|lhs, rhs| lhs.start().cmp(rhs.start()));
    for range in ranges.iter() {
        if !merged.is_empty() && merged.last().unwrap().end() >= range.start() {
            let len_merged = merged.len();
            merged[len_merged - 1] =
                *merged[len_merged - 1].start()..=*range.end().max(merged[len_merged - 1].end());
        } else {
            merged.push(range.clone());
        }
    }
    return merged
        .iter()
        .fold(0, |acc, range| acc + range.end() - range.start() + 1);
}

fn main() {
    let input = std::fs::read_to_string("input.txt").unwrap();
    println!("part 1 {}", part1(&input));
    println!("part 2 {}", part2(&input));
}

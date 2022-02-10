fn main() {
    println!("Hello, world!");
    date_09_02_2022();
}

fn date_09_02_2022 () {
    let arr = [1,2,3,4,5];
    let mut result = [1; 5];
    for item in arr.iter().enumerate() {
        let (index, _): (usize, _) = item;
        for item1 in arr.iter().enumerate() {
            let (index1, elm1): (usize, &i32) = item1;
            if index != index1 {
                result[index] *= elm1;
            }
        }
    }

    println!("{:?}", result)
}

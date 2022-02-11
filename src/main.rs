fn main() {
    println!("Hello, world!");
    date_09_02_2022();
    date_08_02_2022();
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

fn date_08_02_2022 () {
    let arr = [1, 4, 6, 9, 10];
    let k = 10;
    let mut result = Vec::new();

    for item in arr.iter().enumerate() {
        let (inx1, val1) = item;
        for item2 in arr.iter().enumerate() {
            let (inx2, val2) = item2;
            if val1 + val2 == k && inx1 != inx2 {
                if !result.contains(&inx1) && !result.contains(&inx2) {
                    result.push(inx1);
                    result.push(inx2);

                    println!("{} + {} = {}", arr[inx1], arr[inx2], k);
                }
            }
        }
    }

    println!("{:?}", result);
}

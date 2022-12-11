fn merge(arr: &mut Vec<i32>, left: usize, middle: usize, right: usize){
  let mut left_index = left;
  let left_threshold = middle + 1;
  let mut left_flag = false;

  let mut right_index = middle+1;
  let right_threshold = right;
  let mut right_flag = true;

  let mut k = left;
  let mut vector: Vec<i32> = Vec::new();

  loop{
    if(k > right){
      break;
    }

    // left, right 중 어떤 index를 선택할 지 결정한다.
    if(left_index < left_threshold){
      left_flag = true;
    }
    if(right_index <= right_threshold){
      right_flag = true;
    }

    // 
    if(left_flag && right_flag){
      if(arr[left_index] < arr[right_index]){
        vector.push(arr[left_index]);
        left_index += 1;
      }
      else{
        vector.push(arr[right_index]);
        right_index += 1;
      }
    }
    else if(left_flag && !right_flag){
      vector.push(arr[left_index]);
      left_index += 1;
    }
    else if(!left_flag && right_flag){
      vector.push(arr[right_index]);
      right_index += 1;
    }
    left_flag = false;
    right_flag = false;
    k+=1;
  }

  for i in 0..vector.len(){
    arr[left + i] = vector[i];
  }
}
fn merge_sorting(mut arr: &mut Vec<i32>, left: usize, right: usize) {
  if(left < right){
    let middle = (left + right) / 2;
    merge_sorting(arr, left, middle);
    merge_sorting(arr, middle+1, right);
    merge(arr, left, middle, right);
  }
}

// fn main() {
//   let mut v: Vec<i32> = vec![1,7,5,3,2];
//   let length = v.len()-1;
//   merge_sorting(&mut v, 0, length);
// }
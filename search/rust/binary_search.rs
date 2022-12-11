fn binary_search(arr: &mut Vec<i32>, target:i32)->usize{
  arr.sort();
  let mut left: usize = 0;
  let mut right = arr.len();
  let mut middle: usize = 0;
  let mut flag: bool = false;

  loop{
    if(left > right){
      break;
    }
    middle = ((left + right) / 2);
    if(arr[middle] == target){
      flag = true;
      break;
    }
    else if(arr[left] < arr[middle]){
      left += 1;
    }
    else if(arr[right] > arr[middle]){
      right -= 1;
    }
  }

  if(flag){
    return middle;
  }
  else{
    panic!("해당되는 값이 없음");
  }
}
fn partition(arr: &mut Vec<i32>, left: usize, right: usize) -> usize{
  // 1. 피벗 가져오기
  let pivot = arr.get(left).cloned().unwrap();
  let mut row = left + 1;
  let mut high = right;
  let mut LeastOneChangedArray: bool = false;

  // 2. loop를 통해 pivot 계산하기
  loop{
    // 3. left point 계산하기
    // 피벗보다 큰 경우는 right size에 남겨두기
    while ((row <= high) && (pivot > arr.get(row).cloned().unwrap())){
      row += 1;
    }

    // 4. 피벗이 더 큰 경우, 작은 값을 high 가 가리킨다.
    while ((high >= row) && (pivot < arr.get(high).cloned().unwrap())){
      high -= 1;
    }

    // 5. high가 row보다 더 작아진 경우, high 와 pivot의 위치 교환 후 종료
    if (high < row){
      arr.swap(left, high);
      break;
    }
    else{
      LeastOneChangedArray = true;
      arr.swap(row, high);
      row += 1;
      high -= 1;
    }
  }

  if (LeastOneChangedArray){
    // 한 번 이라도 스왑이 된 경우, 피벗 index는 high이다.
    return high
  }
  else{
    return left
  }
}

fn quick_sorting(arr: &mut Vec<i32>, left: usize, right: usize){
  if(left < right){
    let pivot = partition(arr, left, right);
    quick_sorting(arr, left, pivot-1);
    quick_sorting(arr, pivot+1, right);
  }
}

fn main() {
  let mut v: Vec<i32> = vec![2,3,1,5,7,53,34,8];
  let length = v.len()-1;
  let r = quick_sorting(&mut v, 0, length);
}
struct Solution;

impl Solution {
    pub fn sort_matrix(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let (mut diagonals_fw, mut diagonals_bw) = Solution::get_diagonals(&grid);
        
        Solution::print_matrix(&grid);

        println!("{:?}", diagonals_fw);
        println!("{:?}", diagonals_bw);
        
        for diagonal in diagonals_fw.iter_mut() {
            diagonal.sort();
            diagonal.reverse();
        }
        
        for diagonal in diagonals_bw.iter_mut() {
            diagonal.sort();
        }

        println!("{:?}", diagonals_fw);
        println!("{:?}", diagonals_bw);
        
        let res = Solution::reassemble_matrix(&diagonals_fw, &diagonals_bw);

        Solution::print_matrix(&grid);

        return res;
    }
    
    pub fn get_diagonals(grid: &Vec<Vec<i32>>) -> (Vec<Vec<i32>>, Vec<Vec<i32>>) {
        let mut diagonals_fw: Vec<Vec<i32>> = Vec::new();
        let mut diagonals_bw: Vec<Vec<i32>> = Vec::new();
        let rows = grid.len();
        let cols = grid[0].len();
        
        for r in 0..rows {
            let mut diagonal: Vec<i32> = Vec::new();
            let mut x = r;
            let mut y = 0;
            while x < rows && y < cols {
                diagonal.push(grid[x][y]);
                x += 1;
                y += 1;
            }
            diagonals_fw.push(diagonal);
        }
        
        for c in 1..cols {
            let mut diagonal: Vec<i32> = Vec::new();
            let mut x = 0;
            let mut y = c;
            while x < rows && y < cols {
                diagonal.push(grid[x][y]);
                x += 1;
                y += 1;
            }
            diagonals_bw.push(diagonal);
        }
        
        
        return (diagonals_fw, diagonals_bw);
        
    }
    
    pub fn print_matrix(grid: &Vec<Vec<i32>>) {
        for row in grid {
            println!("{:?}", row);
        }
    }
    
    pub fn reassemble_matrix(dfw: &Vec<Vec<i32>>, dbw: &Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let rows = dfw.len();
        let cols = rows;

        let mut result: Vec<Vec<i32>> = vec![vec![0; cols]; rows];
        
        for r in 0..rows {
            let mut x = r;
            let mut y = 0;
            let mut d = 0;
            while x < rows && y < cols {
                result[x][y] = dfw[r][d];
                x += 1;
                y += 1;
                d += 1;
            }
        }
        
        for c in 1..cols {
            let mut x = 0;
            let mut y = c;
            let mut d = 0;
            while x < rows && y < cols {
                result[x][y] = dbw[c-1][d];
                x += 1;
                y += 1;
                d += 1;
            }
        }
        
        return result;
    }

}

fn main() {
    let raw_grid = [[1,7,3],[9,8,2],[4,5,6]];
    let grid: Vec<Vec<i32>> = raw_grid.iter().map(|row| row.to_vec()).collect();
    let result = Solution::sort_matrix(grid.clone());
}

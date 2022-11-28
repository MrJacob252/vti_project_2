use pyo3::prelude::*;
mod prime_gen;

// Ukazkova fce
/// Formats the sum of two numbers as string.
// #[pyfunction]
// fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
//     Ok((a + b).to_string())
// }

#[pyfunction]
fn prime_num_gen() -> PyResult<Vec<u128>> {
    //! Call to the prime generating module
    let prime_list:Vec<u128> = prime_gen::main_primes();
    Ok(prime_list)  
}

/// A Python module implemented in Rust.
#[pymodule]
fn vti_project_2(_py: Python, m: &PyModule) -> PyResult<()> {
    // m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(prime_num_gen, m)?)?;
    Ok(())
}


//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
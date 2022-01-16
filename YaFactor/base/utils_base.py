from scipy.linalg import svd

def compute_svd(X,lapack_driver='gesdd'):
    """Computes an SVD with k components, based on Lapack librairies
     via Scipy 
    Parameters
        ----------
    X : array of float, a table containing numeric values.

    lapack_driver : {'gesdd', 'gesvd'}, optional
        Whether to use the more efficient divide-and-conquer approach
        (``'gesdd'``) or general rectangular approach (``'gesvd'``)
        to compute the SVD. MATLAB and Octave use the ``'gesvd'`` approach.
        Default is ``'gesdd'``

    Returns
        -------
    U : ndarray
        Unitary matrix having left singular vectors as columns.
        Of shape ``(M, M)`` M = nrow(X).
    s : ndarray
        The singular values, sorted in non-increasing order.
        Of shape (K,), with ``K = ncol(X))``.
    V : ndarray
        Unitary matrix having right singular vectors as rows.
        Of shape ``(N, N)`` or N = ncol(X)
        """
    U,S, V = svd(X, full_matrices=False,lapack_driver='gesdd')
    
    return U,S,V





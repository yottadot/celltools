import numpy as np
from numpy.linalg import inv

class basis_transformation:
    def __init__(self, basis1, basis2):
        """

        :param start_basis:
        :param target_basis:
        """
        self.t_matrix = np.ones((3,3))
        self.invt_matrix = inv(self.t_matrix)

        pass

    def transform(self, v):
        """
        transforms vector v in basis1 coordinates to coordinates in basis2
        :param v: nd.array of shape (3,)
        :return: nd.array of shape (3,)
        """
        pass

    def inv_transform(self, v):
        """
        transforms vector v in basis2 coordinates to coordinates in basis1
        :param v: nd.array of shape (3,)
        :return: nd.array of shape (3,)
        """
        pass
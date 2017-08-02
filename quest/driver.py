"""
Drives modules
"""

from . import mp2
from . import scf_module
from . import molecule
from . import wavefunction
from .response import response


def compute_scf_response(wavefunction):
    return response(wavefunction)


def compute_mp2(wavefunction):
    return mp2.mp2(wavefunction)


def compute_rhf(mol, basis_name="aug-cc-pvdz", numpy_memory=1.e9, maxiter=12, E_conv=1.e-6, D_conv=1.e-4):
    mol = molecule.Molecule(mol, basis_name)
    wfn = wavefunction.Wavefunction(mol, {})

    # Compute RHF
    scf_energy = scf_module.compute_rhf(wfn, df=False, diis=False)
    return (scf_energy, wfn)


def compute_mc(sigma, epsilon, coord_file_path, params):
    pass

class Grid():

    def __init__(self, random_things):
        self.random_things = random_things

    def _plot_grid(self, x_span, y_span):
        r"""
        Plot a random grid randomly generated in a random day by someone
        somewhat random.

        Parameters
        ----------
        x_span : numpy array
            Spanned values of x-axis (not randomly oriented).
        y_span : numpy array
            Sppaned values of y-axis (this one can be random).

        Returns
        -------
        axes : numpy array
            The plot axes. 

        Notes
        -----
        Hope you don't mind if I write too much on this documentation. 
        You know, documentation is the kind of thing you never complain 
        with. The more, the better [2]_.

        .. math::
          e^{i\pi} + 1 = 0

        Examples
        --------
        >>> print('Olá')
        Olá


        References
        ----------
        .. [2] Random Person that wrote important things concerning
          documentation.

        """
        return None
        
class MassProfile:
    r"""Generic class to specify dark matter profiles.
    
    Parameters
    ----------
    r_s : float
        Scale radius (kpc).
    rho_s: float
        Scale density (GeV/cm^3).
    """
    def __init__(self, r_s, rho_s):
        self.r_s = r_s
        self.rho_s = rho_s
        self._r_sun = 8.33
        self._rho_sun = 0.3
             
    def annihilation_j_factor(self, theta, epsrel=1e-3):
        expr = lambda s: (1/self._r_sun)*(self.density(s, theta, geocentric=True)/self._rho_sun)**2
        j_factor, err = integrate.quad(expr, 0, np.inf, epsrel=epsrel)
        return j_factor, err
    
    def decay_j_factor(self, theta, epsrel=1e-3):
        expr = lambda s: (1/self._r_sun)*(self.density(s, theta, geocentric=True)/self._rho_sun)    
        j_factor, err = integrate.quad(expr, 0, np.inf, epsrel=epsrel)
        return j_factor, err
    
    def _galactocentric_to_geocentric(self, r, theta):
        return np.sqrt(self._r_sun**2 + r**2 - 2*r*self._r_sun*np.cos(theta))

class NFWDisk(MassProfile):
    r"""Navarro-Frenk-White (NFW) dark matter denstiy
    profile. See [1]_ for more information.

    Parameters
    ----------
    r_s : float
        Scale radius (kpc).
    rho_s: float
        Scale density (GeV/cm³).


    .. math::
        \rho_{\mathrm{NFW}}(r) = \dfrac{\rho_s}{\dfrac{r}{r_s} \left(1+\dfrac{r}{r_s} \right)^2}
        

    References
    ----------
    .. [1] PPPC 4 DM ID: A Poor Particle Physicist Cookbook for Dark Matter Indirect Detection - Marco Cirelli *et al.*
    """
    def __init__(self, r_s=24.42, rho_s=0.184):
        return None

    def density(self, r, theta=None, geocentric=False):
        if geocentric:
            r = self._galactocentric_to_geocentric(r, theta)
        return self.rho_s/((r/self.r_s)*(1+r/self.r_s)**2)
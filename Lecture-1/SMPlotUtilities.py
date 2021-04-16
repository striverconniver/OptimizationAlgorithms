###############################################################################
# @file PlotUtilities.py
#
# @brief Helper utilities for plots
#
# @author Subhashis Mohanty
# @date March 1, 2021
###############################################################################

###############################################################################
# NOTE: THE CODE IN THIS FILE IS NOT PRODUCTION-READY. AMONG OTHER THINGS,
# THIS CODE HAS DUPLICATIONS AND HASN'T BEEN OPTIMIZED.
#
# CAVEAT EMPTOR
###############################################################################

import numpy as np
import matplotlib.transforms as mtransforms
from matplotlib.patches import FancyBboxPatch

###############################################################################
# Main plot details
###############################################################################
mpSize = {"w" : 28/2.54, "h" : 22.4/2.54}
mpRndBnds = {"xl" : -0.15, "xr" : 3.15, "yb" : -0.4, "yt" : 3.15}
mpBnds =  {"xl" : mpRndBnds["xl"] - 0.1,
           "xr" : mpRndBnds["xr"] + 0.1,
           "yb" : mpRndBnds["yb"] - 0.1,
           "yt" : mpRndBnds["yt"] + 0.1}
mpPts = {"x1" : np.arange(-0.25, 3.25, 0.01),
         "x2" : np.arange(-0.25, 3.25, 0.01)}
mpCapLoc = {"hloc" : 1.75, "vloc" : -1}
mpC1 = {"rng" : np.arange(0.9, 3.1, 0.01),
        "cap" : "Figure 2: Bivariate, uncorrelated, translated normal distribution - Level set curves,  with $c_1$ added",
        "ineq" : "$\mathbf{c_1: x_2 \geq 2x_1 - 2}$",
        "tattr" : {"color" : "orange", "fontweight" : "bold", "fontsize" : "large"},
        "attr" : {"color" : "orange", "lw" : 2, "zorder" : 5},
        "txtx" : 0.1,
        "txty" : -0.15
        }

mpC2 = {"rng" : np.arange(0.9, 3.1, 0.01),
        "cap" : "Figure 5: Bivariate, uncorrelated, translated normal distribution - Level set curves,  with $c_1$, $c_2$ added",
        "ineq" : "$\mathbf{c_2: x_2 \leq -2(x_1 - 2)^2 + 2}$",
        "tattr" : {"color" : "red", "fontweight" : "bold", "fontsize" : "large"},
        "attr" : {"color" : "red", "lw" : 2, "zorder" : 10},
        "txtx" : 1.9,
        "txty" : -0.35,
        "arrowsx" : 0.5,
        "arrowsy" : 1.2,
        "arrowdx" : 0.75,
        "arrowdy" : -0.25,
        "fsx" : 0.25,
        "fsy" : 1.25,
        "spx" : 1.0,
        "spy" : 0.0,
        "sptx" : 1.05,
        "spty" : -0.15,
        "sptxt" : "(1, 0) minimizes $\mathbf{f}$ in the feasible region"
        }

pCol = {"Y" : "yellow", "DB" : "DodgerBlue", "R" : "Red", "Y" : "Yellow"}

###############################################################################
# Square function details
###############################################################################
sfRndBnds = {"xl" : -2.15, "xr" : 4.9, "yb" : -2.15, "yt" : 4.9}
sf = {"rngb" : np.arange(-2.25, 2.235, 0.01),
      "ebx" : -1.5,
      "eby" : 4,
      "tbx" : 2,
      "tby" : 2,
      "eqb" : "$\mathbf{x_2 = x_1^2}$",
      "tb" : "This area populated in Figure 4",            
      #
      "rng1" : np.arange(-0.22, 4.235, 0.01),
      "t1tx" : 3.75,
      "t1ty" : 1.8,
      "t1t" : "Step 1",
      "t1x" : 3.75,
      "t1y" : 1.2,
      "t1" :  "(translated)",     
      "e1x" : 3.75,
      "e1y" : 1.5,
      "eq1" : "$\mathbf{x_2 = (x_1 - 2)^2}$",
      #
      "t2tx" : 0.65,
      "t2ty" : 4.5,
      "t2t" : "Step 2",
      "t2x" : 0.65,
      "t2y" : 3.9,
      "t2" :  "(translated, scaled)",
      "e2x" : 0.65,
      "e2y" : 4.2,
      "eq2" : "$\mathbf{x_2 = 2(x_1 - 2)^2}$",
      #
      "t3tx" : 1.18,
      "t3ty" : -1.55,
      "t3t" : "Step 3",
      "t3x" : 1.18,
      "t3y" : -2.15,
      "t3" :  "(translated, scaled, inverted)",
      "e3x" : 1.18,
      "e3y" : -1.85,
      "eq3" : "$\mathbf{x_2 = -2(x_1 - 2)^2}$",
      #
      "t4tx" : 3.1,
      "t4ty" : 0.1,
      "t4t" : "Step 4",
      "t4x" : 3.2,
      "t4y" : -0.52,
      "t4" :  "(translated, scaled,",
      "t4bx" : 3.3,
      "t4by" : -0.72,      
      "tb" :  "inverted, translated)",      
      "e4x" : 3.2,
      "e4y" : -0.22,
      "eq4" : "$\mathbf{x_2 = -2(x_1 - 2)^2} + 2$",
      "e4sx" : 3.4,
      "e4sy" : -1.12,
      "eqs4" : "= $\mathbf{c_2^{equality}}$",
      "e4px" : 1.8,
      "e4py" : 2.2,
      "eqp4" : "(2, 2)",
      "e4tx" : 2.0,
      "e4ty" : 2.0,
      #
      "tattrC" : {"color" : "Chartreuse", "fontweight" : "bold", "fontsize" : "large"},
      "tattrCs" : {"color" : "Chartreuse", "fontsize" : "large"},
      #
      "tattrY" : {"color" : "yellow", "fontweight" : "bold", "fontsize" : "large"},
      "tattrYs" : {"color" : "yellow", "fontweight" : "bold", "fontsize" : "large"},      
      "Y" : {"color" : "yellow"},
      #
      "tattrDB" : {"color" : "DodgerBlue", "fontweight" : "bold", "fontsize" : "large"},
      "tattrDBs" : {"color" : "DodgerBlue", "fontweight" : "bold", "fontsize" : "large"},
      "DB" : {"color" : "DodgerBlue"},
      #
      "tattrHP" : {"color" : "HotPink", "fontweight" : "bold", "fontsize" : "large"},
      "tattrHPs" : {"color" : "HotPink", "fontweight" : "bold", "fontsize" : "large"},      
      "HP" : {"color" : "HotPink"},
      #
      "tattrR" : {"color" : "Red", "fontweight" : "bold", "fontsize" : "large"},
      "tattrRs" : {"color" : "Red", "fontweight" : "bold", "fontsize" : "large"},      
      "R" : {"color" : "Red"},
      #
      "cap" : "Figure 3: The Square Function",
      "cap2" : "Figure 4: The translated, scaled , inverted, and translated again Square Function"
      }
sfBnds =  {"xl" : sfRndBnds["xl"] - 0.1,
           "xr" : sfRndBnds["xr"] + 0.1,
           "yb" : sfRndBnds["yb"] - 0.1,
           "yt" : sfRndBnds["yt"] + 0.1}
sfCapLoc = {"hloc" : 1.33, "vloc" : -3.25}
###############################################################################

def EnvelopeRounded(ax, xl, xr, yb, yt):
    bb = mtransforms.Bbox([[xl, yb], [xr, yt]])
    p_fancy = FancyBboxPatch((bb.xmin, bb.ymin),
                             abs(bb.width), abs(bb.height),
                             boxstyle="round,pad=0.1",
                             fc=(0., 0., 0.),
                             ec=(1., 1., 1.),zorder=-10)
    ax.add_patch(p_fancy)

def EnvelopeRoundedCompact(ax, d):
    bb = mtransforms.Bbox([[d["xl"], d["yb"]], [d["xr"], d["yt"]]])
    p_fancy = FancyBboxPatch((bb.xmin, bb.ymin),
                             abs(bb.width), abs(bb.height),
                             boxstyle="round,pad=0.1",
                             fc=(0., 0., 0.),
                             ec=(1., 1., 1.),zorder=-10)
    ax.add_patch(p_fancy)    

title_font = {'fontname':'Arial', 'size':'16', 'color':'black',
              'weight':'normal', 'verticalalignment':'bottom'} 
axis_font = {'fontname':'Arial', 'size':'14'}    

def SetupPlot(ax, plt, xlbl, ylbl, xl, xr, yb, yt, title, faux_title, hloc,
              vloc):
    ax.text(hloc, vloc, faux_title, ha='center', **title_font)
    ax.set_title(title, **title_font)
    ax.set_xlabel(xlbl, **axis_font)
    ax.set_ylabel(ylbl, **axis_font)
    ax.set(xlim=(xl, xr), ylim=(yb, yt))
    ax.grid(color="w", linestyle="-", linewidth=0.2)
    ###########################################################################
    # Suppress the axes spines
    ###########################################################################
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)    
    ###########################################################################
    # Draw our own axes
    ###########################################################################
    DrawArrow(plt, xl, 0, xr - xl, 0, 'white', 0.5, 0.1, True, 0.1)
    DrawArrow(plt, 0, yb, 0, yt - yb, 'white', 0.5, 0.1, True, 0.1)

def SetupPlotCompact(ax, plt, xlbl, ylbl, d, title, faux_title, dcap):
    ax.text(dcap["hloc"], dcap["vloc"], faux_title, ha='center', **title_font)
    ax.set_title(title, **title_font)
    ax.set_xlabel(xlbl, **axis_font)
    ax.set_ylabel(ylbl, **axis_font)
    ax.set(xlim=(d["xl"], d["xr"]), ylim=(d["yb"], d["yt"]))
    ax.grid(color="w", linestyle="-", linewidth=0.2)
    ###########################################################################
    # Suppress the axes spines
    ###########################################################################
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)    
    ###########################################################################
    # Draw our own axes
    ###########################################################################
    DrawArrow(plt, d["xl"], 0, d["xr"] - d["xl"], 0, 'white', 0.5, 0.1, True,
              0.1)
    DrawArrow(plt, 0, d["yb"], 0, d["yt"] - d["yb"], 'white', 0.5, 0.1, True,
              0.1)    

def DrawArrow(plt, x, y, dx, dy, color, lw, headWid, incHeadLen, headLen):
    plt.arrow(x, y, dx, dy, lw=lw, color=color, head_width=headWid,
              length_includes_head=incHeadLen, head_length=headLen)

###############################################################################
# Initialize N - the normalization constant for an uncorrelated (i.e. rho = 0),
# unit variance (i.e. sigma_x1 = 1, sigma_x2 = 1) this value of N ensures
# that the PDF integrates to 1 over all # x1 and x2
###############################################################################
N = 1/(2 * np.pi)

###############################################################################
# Given values for x1, mux1, y_1, return the value of the PDF. We will use
# a set of returned values of this function to create contour plots
###############################################################################
def fv(x1, mux1, x2, mux2):
    return N * np.exp(-((x1 - mux1)**2 + (x2 - mux2)**2)/2)    

def BivariateNormal(x1_points, x2_points):
    ###########################################################################
    x1, x2 = np.meshgrid(x1_points, x2_points)
    ###########################################################################
    # Initialize the PDF
    ###########################################################################
    f = N * np.exp(-((x1 - 1)**2 + (x2 - 2)**2)/2)
    ###########################################################################
    # This list picks a few values of the pdf to feed into the contour plots
    ###########################################################################
    levellist = [fv(1,1,0,2), N/4, fv(2.25, 1, 2, 2), N/1.1, N/1.01, N]
    ###########################################################################
    return x1, x2, f, levellist
    ###########################################################################

def BivariateNormalCompact(d):
    ###########################################################################
    x1, x2 = np.meshgrid(d["x1"], d["x2"])
    ###########################################################################
    # Initialize the PDF
    ###########################################################################
    f = N * np.exp(-((x1 - 1)**2 + (x2 - 2)**2)/2)
    ###########################################################################
    # This list picks a few values of the pdf to feed into the contour plots
    ###########################################################################
    levellist = [fv(1,1,0,2), N/4, fv(2.25, 1, 2, 2), N/1.1, N/1.01, N]
    ###########################################################################
    return x1, x2, f, levellist
    ###########################################################################    

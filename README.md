# Read Me
Superlattice fitting project on LSMO/LNO superlattice on STO substrates.

## Problems
* -- fitting worse that ++
* Need major work for +-
* Need to use DREAM feature for uncertainty analysis
 
## To do list

## Naming structure
Naming: sample(ft,n3n1,t5)-magfield(0t,1t)-magfitting9(y,n)-anglefitting(y,n)-notes
Eg. ft-0t-n-n-perfectfit (Fifteen-0T-no magnetic or angle fitting-prefectfitting to data)

## Notes
Stock Command
refl1d --fit=amoeba --steps=1000 --starts=20 --parallel=0 <file>.py --store= --plot=log --view=log
PNR data definitions: ~reflA --, reflB -+, reflC +-, reflD ++

For Jackson reference:
If using VS Code, need to be in right terminal (base anaconda terminal)
Need to run termimal in the same folder as the program.
C:/ProgramData/Anaconda3/Scripts/activate
conda activate base

## Program Options:

    --preview
        display model but do not perform a fitting operation
    --pars=filename or store path
        initial parameter values; fit results are saved as path/<modelname>.par
    --plot=log      [linear|log|residuals]
        type of plot to display
    --simulate
        simulate a dataset using the initial problem parameters
    --simrandom
        simulate a dataset using random problem parameters
    --shake
        set random parameters before fitting
    --noise=5%
        percent noise to add to the simulated data
    --seed=integer
        random number seed
    --err
        show uncertainty estimate from curvature at the minimum
    --cov
        show the covariance matrix for the model when done
    --entropy
        compute entropy for the model when done [dream only]
    --staj
        output staj file when done
    --edit
        start the gui
    --view=linear|log
        one of the predefined problem views; reflectometry also has fresnel,
        logfresnel, q4 and residuals

    --store=path
        output directory for plots and models
    --overwrite
        if store already exists, replace it
    --resume=path    [dream]
        resume a fit from previous stored state
    --parallel=n
        run fit using multiprocessing for parallelism; use --parallel=0 for all cpus
    --mpi
        run fit using MPI for parallelism (use command "mpirun -n cpus ...")
    --batch
        batch mode; save output in .mon file and don't show plots after fit
    --noshow
        semi-batch; send output to console but don't show plots after fit
    --remote
        queue fit to run on remote server
    --notify=user@email
        remote fit notification
    --queue=http://reflectometry.org
        remote job queue
    --time=inf
        run for a maximum number of hours

    --fit=amoeba    [amoeba|de|dream|lm|mp|newton|ps|pt|rl|snobfit]
        fitting engine to use; see manual for details
    --steps=400    [amoeba|de|dream|lm|mp|newton|ps|pt|rl|snobfit]
        number of fit iterations after any burn-in time
    --samples=1e4   [dream]
        set steps so the target number of samples is drawn
    --xtol=1e-4     [de, amoeba]
        minimum population diameter
    --ftol=1e-4     [de, amoeba]
        minimum population flatness
    --pop=10        [dream, de, rl, ps]
        population size
    --burn=100      [dream, pt]
        number of burn-in iterations before accumulating stats
    --thin=1        [dream]
        number of fit iterations between steps
    --nT=25
    --Tmin=0.1
    --Tmax=10       [pt]
        temperatures vector; use a higher maximum temperature and a larger
        nT if your fit is getting stuck in local minima
    --CR=0.9        [de, rl, pt]
        crossover ratio for population mixing
    --starts=1      [newton, rl, amoeba]
        number of times to run the fit from random starting points.
    --keep_best
        when running with multiple starts, restart from a point near the
        last minimum rather than using a completely random starting point.
    --init=eps      [dream]
        population initialization method:
          eps:    ball around initial parameter set
          lhs:    latin hypercube sampling
          cov:    normally distributed according to covariance matrix
          random: uniformly distributed within parameter ranges
    --stepmon
        show details for each step
    --resynth=0
        run resynthesis error analysis for n generations

    --time_model
        run the model --steps times in order to estimate total run time.
    --profile
        run the python profiler on the model; use --steps to run multiple
        models for better statistics
    --chisq
        print the model description and chisq value and exit
    -m/-c/-p command
        run the python interpreter with bumps on the path:
            m: command is a module such as bumps.cli, run as __main__
            c: command is a python one-line command
            p: command is the name of a python script
    -i
        start the interactive interpreter
    -?/-h/--help
        display this help
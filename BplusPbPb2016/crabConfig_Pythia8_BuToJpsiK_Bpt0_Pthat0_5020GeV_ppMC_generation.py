from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'Pythia8PP_BuToJpsiK_Bpt0_Pthat5_5020GeV'
config.General.workArea = 'Banawork'
config.General.transferOutputs = True
config.General.transferLogs = True ###False

config.JobType.pluginName = 'PrivateMC'	###Analysis, modi 1
config.JobType.psetName = 'Pythia8_BuToJpsiK_Bpt0_Pthat5_TuneCUEP8M1_5020GeV_revised_pp_GEN_SIM_re5.py'
config.JobType.inputFiles = ['rssLimit']

config.Data.outputPrimaryDataset = 'Pythia8_BuToJpsiK_5020GeV_PP' ### modi 2
config.Data.splitting = 'EventBased'###Not FileBased
config.Data.unitsPerJob = 100000
NJOBS = 10000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/hckim'
config.Data.publication = True
config.Data.outputDatasetTag = 'Pythia8PP_BuToJpsiK_Bpt0_Pthat5_5020GeV'

config.Site.storageSite = 'T2_KR_KNU'





# Auto generated configuration file
# using: 
# Revision: 1.381.2.13 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/HIBana/HIJINGemb_BuJpsiK_TuneZ2star_5TeV_cff --conditions STARTHI53_V27::All -s GEN,SIM --process HISIGNAL -n 10 --eventcontent RAWSIM --datatier GEN-SIM --relval None --filein file:/afs/cern.ch/work/h/hckim/CMSSW_5_3_14/src/UserCode/MCtest/localRun/E6C7EEFE-E567-E211-BFD6-00A0D1E952FC.root --scenario HeavyIons --himix --beamspot Match8TeVCollisionPPbBoost
import FWCore.ParameterSet.Config as cms

process = cms.Process('HISIGNAL')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('SimGeneral.MixingModule.HiEventMixing_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('GeneratorInterface.HiGenCommon.VtxSmearedMatchPPbBoost8TeVCollision_cff')
process.load('SimGeneral.MixingModule.himixGEN_cff')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('SimGeneral.MixingModule.himixSIMIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring('file:/afs/cern.ch/work/h/hckim/CMSSW_5_3_14/src/UserCode/MCtest/localRun/E6C7EEFE-E567-E211-BFD6-00A0D1E952FC.root'),
    inputCommands = cms.untracked.vstring('drop *', 
        'keep *_generator_*_*', 
        'keep *_g4SimHits_*_*'),
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False)
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    annotation = cms.untracked.string('B+ -> Jpsi K+ at 5TeV for embedding on HIJING'),
    name = cms.untracked.string('$Source: /local/projects/CMSSW/rep/CMSSW/Configuration/GenProduction/python/PYTHIA6_Bu2JpsiK_TuneZ2_7TeV_cff.py,v $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('HIJINGemb_BuJpsiK_TuneZ2star_5TeV_cff_GEN_SIM.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'STARTHI53_V27::All', '')

process.hiSignal = cms.EDFilter("PyquenGeneratorFilter",
    ExternalDecays = cms.PSet(
        EvtGen = cms.untracked.PSet(
            use_default_decay = cms.untracked.bool(False),
            decay_table = cms.FileInPath('GeneratorInterface/ExternalDecays/data/DECAY_NOLONGLIFE.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/evt.pdl'),
            user_decay_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/Bu_JpsiK.dec'),
            list_forced_decays = cms.vstring('MyB+', 
                'MyB-'),
            operates_on_particles = cms.vint32(0)
        ),
        parameterSets = cms.vstring('EvtGen')
    ),
    etaMin = cms.double(-3.0),
    comEnergy = cms.double(5023.0),
    minimumCandidates = cms.int32(1),
    etaMax = cms.double(3.0),
    doCollisionalEnLoss = cms.bool(False),
    doQuench = cms.bool(False),
    qgpInitialTemperature = cms.double(1.0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    backgroundLabel = cms.InputTag("generator"),
    angularSpectrumSelector = cms.int32(0),
    ptMin = cms.double(0.0),
    hadronFreezoutTemperature = cms.double(0.14),
    status = cms.int32(1),
    qgpNumQuarkFlavor = cms.int32(0),
    doRadiativeEnLoss = cms.bool(True),
    bFixed = cms.double(0.0),
    doIsospin = cms.bool(True),
    filterType = cms.untracked.string('BpCandGenEvtSelector'),
    bMin = cms.double(0.0),
    numQuarkFlavor = cms.int32(0),
    cFlag = cms.int32(0),
    protonSide = cms.untracked.int32(2),
    bMax = cms.double(0.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(33)=0     ! no K factors in hard cross sections', 
            'MSTP(2)=1      ! which order running alphaS', 
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
            'MSTP(52)=2     ! work with LHAPDF', 
            'PARP(82)=1.921 ! pt cutoff for multiparton interactions', 
            'PARP(89)=1800. ! sqrts for which PARP82 is set', 
            'PARP(90)=0.227 ! Multiple interactions: rescaling power', 
            'MSTP(95)=6     ! CR (color reconnection parameters)', 
            'PARP(77)=1.016 ! CR', 
            'PARP(78)=0.538 ! CR', 
            'PARP(80)=0.1   ! Prob. colored parton from BBR', 
            'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter', 
            'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter', 
            'PARP(62)=1.025 ! ISR cutoff', 
            'MSTP(91)=1     ! Gaussian primordial kT', 
            'PARP(93)=10.0  ! primordial kT-max', 
            'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4     ! Defines the multi-parton model'),
        bbbarSettings = cms.vstring('MSEL = 1'),
        parameterSets = cms.vstring('pythiaUESettings', 
            'bbbarSettings')
    ),
    embeddingMode = cms.bool(True),
    aBeamTarget = cms.double(208.0),
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    qgpProperTimeFormation = cms.double(0.1),
    pdg = cms.int32(521)
)


process.ProductionFilterSequence = cms.Sequence(process.hiSignal)

# Path and EndPath definitions
#process.generation_step = cms.Path(process.pgen_himix)
process.generation_step = cms.Path(process.pgen_hi)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 


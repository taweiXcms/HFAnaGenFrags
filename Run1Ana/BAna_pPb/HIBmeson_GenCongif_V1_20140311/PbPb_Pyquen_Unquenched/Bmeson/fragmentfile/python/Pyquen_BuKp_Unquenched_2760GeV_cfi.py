import FWCore.ParameterSet.Config as cms


from Configuration.Generator.PyquenTuneZ2Settings_cff import *

hiSignal = cms.EDFilter("PyquenGeneratorFilter",
    ptMin = cms.double(5.0),
    etaMax = cms.double(3.0),
    etaMin = cms.double(-3.0),
	pdg = cms.int32(521),
	dau2pdg = cms.int32(321),
	dau2dau1pdg = cms.int32(0),
	dau2dau2pdg = cms.int32(0),
	status = cms.int32(1),
    minimumCandidates = cms.int32(1),
    filterType = cms.untracked.string('BpCandGenEvtSelector'),
    aBeamTarget = cms.double(208.0),
    comEnergy = cms.double(2760.0),
    qgpInitialTemperature = cms.double(1.0),
    doCollisionalEnLoss = cms.bool(False),
    qgpNumQuarkFlavor = cms.int32(0),
    qgpProperTimeFormation = cms.double(0.1),
    numQuarkFlavor = cms.int32(0),
    hadronFreezoutTemperature = cms.double(0.14),
    doRadiativeEnLoss = cms.bool(True),
    backgroundLabel = cms.InputTag("generator"),
	embeddingMode = cms.bool(True),
    angularSpectrumSelector = cms.int32(0),
    doIsospin = cms.bool(True),
    doQuench = cms.bool(False),
    cFlag = cms.int32(0),
    bFixed = cms.double(0.0),
    bMin = cms.double(0.0),
    bMax = cms.double(0.0),
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
#    maxEventsToPrint = cms.untracked.int32(0),
#    pythiaPylistVerbosity = cms.untracked.int32(1),
#    pythiaHepMCVerbosity = cms.untracked.bool(True),
#    protonSide = cms.untracked.int32(0), #Take into account whether it's a nn or pp or pn interaction
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
    )
)

ProductionFilterSequence = cms.Sequence(hiSignal)

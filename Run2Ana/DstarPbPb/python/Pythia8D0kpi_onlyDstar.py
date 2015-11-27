import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(5020.0),
    maxEventsToPrint = cms.untracked.int32(0),
    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2010.DEC'),
            operates_on_particles = cms.vint32(),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
            user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/Dstar_VSSD0pi_Kpipi.dec'),
            list_forced_decays = cms.vstring('myD*+', 'myD*-')
        ),
        parameterSets = cms.vstring('EvtGen130')
    ),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(     
            'HardQCD:all = on',
            'PhaseSpace:pTHatMin = 15.', #min pthat
        ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CUEP8M1Settings',
            'processParameters',
        )
    )
)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)

Dfilter = cms.EDFilter("MCSingleParticleFilter",
    MaxEta = cms.untracked.vdouble(2.1, 2.1),
    MinEta = cms.untracked.vdouble(-2.1, -2.1),
    MinPt = cms.untracked.vdouble(15.0, 15.0), #min pt
    ParticleID = cms.untracked.vint32(413, -413)
)

DstarDaufilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(0),
    ParticleID = cms.untracked.int32(413),
    DaughterIDs = cms.untracked.vint32(421, 211),
    verbose = cms.untracked.int32(0),
    MinPt = cms.untracked.vdouble(0.0, 0.0),
    MaxEta = cms.untracked.vdouble(9999, 9999),
    MinEta = cms.untracked.vdouble(-9999, -9999),
    NumberDaughters = cms.untracked.int32(2),
)

D0Daufilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(413),
    ParticleID = cms.untracked.int32(421),
    DaughterIDs = cms.untracked.vint32(-321, 211),
    verbose = cms.untracked.int32(0),
    MinPt = cms.untracked.vdouble(0.0, 0.0),
    MaxEta = cms.untracked.vdouble(9999, 9999),
    MinEta = cms.untracked.vdouble(-9999, -9999),
    NumberDaughters = cms.untracked.int32(2),
)

ProductionFilterSequence = cms.Sequence(generator*Dfilter*DstarDaufilter*D0Daufilter)

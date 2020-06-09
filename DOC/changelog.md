
# Changelog
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
- Major Code Refactoring (added focus on Object Oriented Programing)
- Category selector dialog
- VSS log implementation
- SSL log implementation

## [0.3.2] - 2020-06-04

## Added

- getMostRecentTaclerAndPosition function implementation
- statChanged function implementation
- computeAllGoals implementation
- plotBarData class "data structure" implementation

## Modified

- Underlying code structure changed to be more oop centered (classes instead of single .py)


## [0.3.1] - 2020-05-25

## Modified

- RoboCIn and Adversary will now be instances of teamClass
- Any type of event can now be instantiated as an eventClass

## Deprecated

- RoboCIn and Adversary classes wont be used anymore
- Penalties and Faults classes wont be used anymore

## [0.3.0] - 2020-05-23
 
### Added
 
- Class diagram implementation
- Bar plot implementation
- Pie plot implementation
- Scatter plot implementation
- Changelog

### Fixed
  
- View desapearing while switching tabs

## Changed

- createPlot() now won't be responsible for collecting the log's data

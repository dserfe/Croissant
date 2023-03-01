testClass=$1

mvn surefire:test -Drat.skip -Denforcer.skip=true -Dcheckstyle.skip -Dspotbugs.skip -Dsurefire.rerunFailingTestsCount=5 -Dtest=${testClass} -Djacoco.skip 
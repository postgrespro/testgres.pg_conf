# /////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

import logging
import threading

from .TestGlobalResource import TestGlobalResource

# /////////////////////////////////////////////////////////////////////////////
# TestGlobalResource


class TestGlobalCache:
    sm_Guard = threading.Lock()
    sm_Dict: dict[str, any] = dict[str, any]()

    # --------------------------------------------------------------------
    def __init__(self):
        pass

    # --------------------------------------------------------------------
    def GetOrCreateResource(globalResourceID: str, resourceFactory) -> any:
        assert resourceFactory is not None
        assert isinstance(globalResourceID, str)
        assert __class__.sm_Guard is not None
        assert isinstance(__class__.sm_Dict, dict)

        with __class__.sm_Guard:
            if globalResourceID in __class__.sm_Dict.keys():
                r = __class__.sm_Dict[globalResourceID]

                return r

            r = resourceFactory()

            __class__.sm_Dict[globalResourceID] = r
            return r

    # --------------------------------------------------------------------
    def ReleaseAllResources():
        assert __class__.sm_Guard is not None
        assert isinstance(__class__.sm_Dict, dict)

        with __class__.sm_Guard:
            emptyDict = dict[str, any]()

            curDict = __class__.sm_Dict

            __class__.sm_Dict = emptyDict

            for resourceID in curDict.keys():
                assert isinstance(resourceID, str)

                r = curDict[resourceID]

                if not isinstance(r, TestGlobalResource):
                    continue

                assert isinstance(r, TestGlobalResource)

                rr: TestGlobalResource = r

                try:
                    logging.info("Release global resource [{0}]".format(resourceID))

                    rr.ReleaseResource()
                except Exception as e:
                    logging.error(
                        "Failed to release global resource [{0}]. Exception ({1}): {2}.".format(
                            resourceID, type(e).__name__, e
                        )
                    )


# /////////////////////////////////////////////////////////////////////////////

thrashcatcher Product README

  Overview

    This product extends the Zope2 "trace log", adding information about
    how many objects were loaded and stored by the ZODB connection for
    each request.  Object loads are recorded in a new 'L' record type,
    along with a synthesized description of the request.  Stores are
    recorded immediately afterward in a new 'S' record type.

  Example

    Here is what the trace log looks like after starting Zope with the
    product installed and visiting the QuickStart page, followed by the
    ZMI::

        B 158391180 2007-10-11T12:47:19 GET /
        I 158391180 2007-10-11T12:47:19 0
        B 158537420 2007-10-11T12:47:19 GET /manage_page_style.css
        I 158537420 2007-10-11T12:47:19 0
        L 0 2007-10-11T12:47:19          0 (GET /)
        S 0 2007-10-11T12:47:19          0
        A 158391180 2007-10-11T12:47:19 200 2907
        E 158391180 2007-10-11T12:47:19 
        L 0 2007-10-11T12:47:19          0 (GET /manage_page_style.css)
        S 0 2007-10-11T12:47:19          0
        A 158537420 2007-10-11T12:47:19 200 3042
        E 158537420 2007-10-11T12:47:19 
        B 158537964 2007-10-11T12:47:23 GET /manage
        I 158537964 2007-10-11T12:47:23 0
        L 0 2007-10-11T12:47:23          0 (GET /manage)
        S 0 2007-10-11T12:47:23          0
        A 158537964 2007-10-11T12:47:23 401 593
        E 158537964 2007-10-11T12:47:23 
        B 158537516 2007-10-11T12:47:24 GET /manage
        I 158537516 2007-10-11T12:47:24 0
        B 158561068 2007-10-11T12:47:24 GET /manage_top_frame
        I 158561068 2007-10-11T12:47:24 0
        B 158465676 2007-10-11T12:47:24 GET /manage_menu
        I 158465676 2007-10-11T12:47:24 0
        B 158563820 2007-10-11T12:47:24 GET /manage_workspace
        I 158563820 2007-10-11T12:47:24 0
        L 0 2007-10-11T12:47:24          8 (GET /manage_top_frame)
        S 0 2007-10-11T12:47:24          0
        A 158561068 2007-10-11T12:47:24 200 1391
        E 158561068 2007-10-11T12:47:24 
        L 0 2007-10-11T12:47:24          1 (GET /manage_workspace)
        S 0 2007-10-11T12:47:24          0
        A 158563820 2007-10-11T12:47:24 302 356
        E 158563820 2007-10-11T12:47:24 
        B 157939532 2007-10-11T12:47:24 GET /manage_main
        I 157939532 2007-10-11T12:47:24 0
        B 157939884 2007-10-11T12:47:24 GET /p_/zopelogo_jpg
        I 157939884 2007-10-11T12:47:24 0
        L 0 2007-10-11T12:47:24          9 (GET /manage_main)
        S 0 2007-10-11T12:47:24          0
        ...


  Installation

    1. Unpack the tarball in a temporary location.
    
    2. Move the 'thrashcatcher' directory from that location into
       '$INSTANCE_HOME/Products'.
    
    2. Enable the trace logger in '$INSTANCE_HOME/etc/zope.conf', e.g.::

        <logger trace>
         level WARN
         <logfile>
             path $INSTANCE/log/trace.log
             format %(message)s
         </logfile>
        </logger>

    
    3. Restart Zope.

    4. Examine '$INSTANCE_HOME/log/trace.log' for 'L' and 'S' records.

  Feedback

    Please report bugs or problems using the "collector",
      http://agendaless.com/Members/tseaver/software/thrashcatcher/issues

    
